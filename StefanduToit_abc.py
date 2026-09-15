import math


skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    #My own SKUs
    {"sku": "HSG-410", "demand": 600, "cost": 90},
    {"sku": "CLP-070", "demand": 15000, "cost": 1},
]
 
 
def usage_value(demand, cost):
    return demand * cost
 
 
def assign_tier(cum_pct, tier_a_cutoff=80, tier_b_cutoff=95):
    if cum_pct <= tier_a_cutoff:
        return "A"
    elif cum_pct <= tier_b_cutoff:
        return "B"
    else:
        return "C"
 
 
def classify_inventory(skus, tier_a_cutoff=80, tier_b_cutoff=95):

    """
    What the function does:
    Takes a list of SKU dictionaries (each with 'demand' and 'cost'),
    and returns a new list sorted by usage value Tier cutoffs default to
    the standard 80% / 95% Pareto split 
    
    """
    # Step 2 - Calculate usage value per SKU
    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])
 
    # Step 3 - Sort descending by value
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)
 
    # Step 4 - Calculate cumulative percentage
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
 
    # Step 5 - Assign a tier
    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"], tier_a_cutoff, tier_b_cutoff)
 
    return skus_sorted
 
 
def print_report(classified_skus):
    for item in classified_skus:
        print(item["sku"], "| value:", item["value"],
              "| cum %:", round(item["cum_pct"], 1),
              "| tier:", item["tier"])
 
    tier_counts = {"A": 0, "B": 0, "C": 0}
    for item in classified_skus:
        tier_counts[item["tier"]] += 1
    print(tier_counts)
 
 
#80% / 95% thresholds
print("=== Standard thresholds (80% / 95%) ===")
classified_standard = classify_inventory(skus, tier_a_cutoff=80, tier_b_cutoff=95)
print_report(classified_standard)
 
#70% / 90% thresholds
print("\n=== Tighter thresholds (70% / 90%) ===")
classified_tight = classify_inventory(skus, tier_a_cutoff=70, tier_b_cutoff=90)
print_report(classified_tight)

#What changed:
""" 
As we can see, the tighter thresholds have resulted in more SKUs being classified as C, and fewer SKUs being classified as A. 
This is because the tighter thresholds require a higher cumulative percentage to be classified as A or B, 
which means that more SKUs fall into the C category.
"""
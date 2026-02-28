from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

def main():
    # Phase 1: Authentication
    credential = AzureCliCredential()
    subscription_id = "YOUR_SUBSCRIPTION_ID_HERE" 
    resource_client = ResourceManagementClient(credential, subscription_id)
    
    print("Successfully authenticated using Azure CLI.")
    print("Fetching resource groups and auditing tags...\n")
    
    resource_groups = resource_client.resource_groups.list()
    
    # Define mandatory tags as a Python 'set'. 
    mandatory_tags = {"customer", "env", "market", "product"}
    
    # Keeps a list of our findings to print a clean summary at the end. Each item will be a dictionary with 'name' and 'missing' keys.
    non_compliant_rgs = []

    # Phase 2 & 3: Extraction and Auditing
    for rg in resource_groups:
        rg_name = rg.name
        rg_tags = rg.tags or {} 
        
        # Extract just the keys (the tag names) from the resource group
        current_tag_keys = set(rg_tags.keys())
        
        # Find the difference between the mandatory set and the current set
        missing_tags = mandatory_tags - current_tag_keys
        
        # 4. If the missing_tags set is not empty, log it
        if missing_tags:
            non_compliant_rgs.append({
                "name": rg_name,
                "missing": missing_tags
            })

    # Phase 4: Output the Report
    print("=== AUDIT REPORT ===")
    if not non_compliant_rgs:
        print("All resource groups are fully compliant.")
    else:
        print(f"Found {len(non_compliant_rgs)} non-compliant resource groups:\n")
        for item in non_compliant_rgs:
            # .join() combines the missing tags into a single comma-separated string
            missing_str = ", ".join(item["missing"])
            print(f"- {item['name']} is missing: {missing_str}")

if __name__ == "__main__":
    main()
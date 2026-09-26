import json
import logging

logging.basicConfig(level=logging.INFO, format='[MaxRF-GlobalGuard] %(asctime)s - %(levelname)s: %(message)s')

class GlobalSovereignGuard:
    def __init__(self, assigned_region: str):
        self.assigned_region = assigned_region.upper()
        # Mock load the legal matrix
        self.sovereign_rules = {
            "EU-EUROPE": {"strict": True, "allowed_destinations": ["eu-central", "eu-west"]},
            "US-DOMESTIC": {"strict": False, "allowed_destinations": ["any"]}
        }

    def validate_regional_boundary(self, execution_payload_destination: str, data_origin: str) -> bool:
        """
        Validates if an incoming cloud tenant's compute job breaches localized cross-border ordinances.
        """
        region_rule = self.sovereign_rules.get(self.assigned_region, {"strict": True, "allowed_destinations": []})
        
        if region_rule["strict"] and execution_payload_destination not in region_rule["allowed_destinations"]:
            logging.critical(
                f"REGULATORY BREACH BLOCK: Data originating from region {data_origin} cannot "
                f"be exfiltrated to non-compliant server link: {execution_payload_destination}."
            )
            return False # HARD DROP: Bypasses execution to protect compliance integrity
            
        logging.info(f"Compliance clearance verified for payload path under framework: {self.assigned_region}.")
        return True

if __name__ == "__main__":
    # Test Scenario: A European MaxRF device processes data, but a malicious tenant tries routing results to a US datacenter
    guard = GlobalSovereignGuard(assigned_region="EU-Europe")
    clearance = guard.validate_regional_boundary(execution_payload_destination="us-east-1", data_origin="Germany-Munich")
    print(f"Global Operation Authorization Status: {clearance}")

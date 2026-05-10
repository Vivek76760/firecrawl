import json
import re

def firecrawl_financial_extractor(html_text):
    # This logic identifies currency and amounts in messy web data
    data = {"currency": "Unknown", "amount": 0, "priority": "Low"}
    
    # 1. Detect Currency
    if "₹" in html_text or "rs" in html_text.lower():
        data["currency"] = "INR"
    elif "$" in html_text:
        data["currency"] = "USD"
        
    # 2. Extract numbers
    numbers = re.findall(r'\d+(?:,\d+)?', html_text.replace(',', ''))
    if numbers:
        data["amount"] = max([int(n.replace(',', '')) for n in numbers])
        
    # 3. Urgency Check
    if any(word in html_text.lower() for word in ["urgent", "fees", "rent", "deadline"]):
        data["priority"] = "High"
        
    return json.dumps(data, indent=2)

# Test with messy input
messy_web = "Admission Alert: Pay Rs 60,000 fees urgently."
print(firecrawl_financial_extractor(messy_web))

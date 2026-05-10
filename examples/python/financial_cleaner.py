import re
import json

def firecrawl_financial_extractor(html_text):
    """
    Extracts financial data from messy HTML strings.
    Optimized for high-stakes accuracy.
    """
    data = {"currency": "Unknown", "amount": 0, "priority": "Low"}
    
    if "₹" in html_text or "rs" in html_text.lower():
        data["currency"] = "INR"
    elif "$" in html_text:
        data["currency"] = "USD"
        
    numbers = re.findall(r'\d+(?:,\d+)?', html_text.replace(',', ''))
    if numbers:
        # Convert found strings to actual integers
        clean_nums = [int(n.replace(',', '')) for n in numbers]
        data["amount"] = max(clean_nums)
        
    urgent_keywords = ["urgent", "fees", "rent", "deadline"]
    if any(word in html_text.lower() for word in urgent_keywords):
        data["priority"] = "High"
        
    return json.dumps(data, indent=2)

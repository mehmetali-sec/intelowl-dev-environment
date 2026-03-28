# Simple Proof of Concept (PoC) for Financial Phishing Detection
# This will be part of my GSoC 2026 proposal for IntelOwl

def check_phishing_keywords(url):
    # Common keywords used in banking phishing attacks
    suspicious_keywords = ["login", "verify", "account", "bank", "update-password", "customer-id"]
    
    url_lower = url.lower()
    found_keywords = [word for word in suspicious_keywords if word in url_lower]
    
    if found_keywords:
        return f"ALERT: Suspicious keywords found: {found_keywords}"
    return "URL looks clean based on keyword analysis."

# Test cases
test_urls = ["https://secure-bank-login-update.com", "https://google.com"]

for url in test_urls:
    print(f"Scanning: {url} -> {check_phishing_keywords(url)}")

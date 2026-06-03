import whois

domain = input("Enter Domain: ")
info = whois.whois(domain)

print(info)

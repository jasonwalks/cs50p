def main():
    spacecraft = {"name": "James Web Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))
    
def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    
    ==========================
    
    """
    
main()
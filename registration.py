print("Register to vote, your vote is your power to make a change")

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name", "")
        reg_number = party.get("reg_number", 0)
        member_count = party.get("member_count", 0)

        
        if member_count >= 1000:  
            print(f"Party '{party_name}' with registration number '{reg_number}' has enough members for registration.")
        else:
            print(f"Party '{party_name}' with registration number '{reg_number}' does not have enough members for registration.")

parties_list = [
    {"ESC": "Party A", "reg_number": "001", "member_count": 1200},
    {"ATM": "Party B", "reg_number": "002", "member_count": 800},
    {"AASD": "Party C", "reg_number": "003", "member_count": 1500}
    {"ANC": "Party D", "reg_number": "004", "member_count": 2000},
    {"AGANG SA": "Party E", "reg_number": "005", "member_count": 8009},
    {"ALJAMA": "Party F", "reg_number": "006", "member_count":500}
    {"ATA": "Party G", "reg_number": "007", "member_count": 200},
    {"AZAPO": "PartY H", "reg_number": "008", "member_count": 850},
    {"APC": "Party I", "reg_number": "010", "member_count": 1550}
    {"BRA": "Party J", "reg_number": "011", "member_count": 1200},
    {"BLF": "Party K", "reg_number": "012", "member_count": 700},
    {"ZACP": "Party L", "reg_number": "013", "member_count": 150}
    {"CPM": "Party M", "reg_number": "014", "member_count": 400},
    {"CSA": "Party N", "reg_number": "015", "member_count": 800},
    {"COPE": "Party O", "reg_number": "016", "member_count": 100}
    {"DA": "Party P", "reg_number": "017", "member_count": 1000},
    {"DLC": "Party Q", "reg_number": "018", "member_count": 800},
    {"ECCFORUM": "Party R", "reg_number": "019", "member_count": 1500}]
    {"EFF": "Party S", "reg_number": "020", "member_count": 1200},
    {"F4SD": "Party T", "reg_number": "021", "member_count": 800},
    {"FREE DEMS": "Party U", "reg_number": "022", "member_count": 1500}
register_party(parties_list)

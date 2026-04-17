import json
from pathlib import Path
def parse_one_file(file_path):
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    file_data = {
        "file_name": file_path.name,
        "adapters": []
    }

    currant_adapter = None

    for line in lines:
        line = line.strip()
        if "adapter" in line and line.endswith(":"):
            if currant_adapter is not None:
                file_data["adapters"].append(currant_adapter)

            current_adpt ={
                "adapter_name": line.replace(":", ""),
                "description": "",
                "physical_address": "",
                "dhcp_enabled": "",
                "ipv4_address": "",
                "subnet_mask": "",
                "default_gateway": "",
                "dns_servers": []
            }    
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].replace(".", "").strip()
            value = parts[1].strip()

            if "Description" in key:
                currant_adapter["description"] = value
            elif "Physical Address" in key:
                currant_adapter["physical_address"] = value
            elif "DHCP Enabled" in key:
                currant_adapter["dhcp_enabled"] = value    
            elif "IPv4 Address" in key:    
                currant_adapter["ipv4_address"] = value
            elif "Subnet Mask" in key:
                currant_adapter["subnet_mask"] = value  
            elif "Default Gateway" in key:
                if value: currant_adapter["default_gateway"] = value
            elif "DNS Servers" in key:
                if value:
                    currant_adapter["dns_servers"].append(value)    

            elif line and currant_adapter: 
                if line[0].isdigit():    
                    if "192." in line or "127." in line or ":" in line:
                        currant_adapter["dns_servers"].append(line)   

            file_data["adapters"].append(currant_adapter)
            return file_data            

            






def main():
    results = []
    folder = Path(".")
    for file_path in sorted(folder.glob("parser_input_*.txt")):
        file_info = parse_one_file(file_path)
        results.append(file_info)

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

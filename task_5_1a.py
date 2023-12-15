computers = {
    "pc1": {
        "os": "Windows 10",
        "Processor": "ADM Phenom II",
        "ram": "8 Gb",
        "video_card": "NVIDIA GeForce GTX 1660",
        "hard_drive": "1 TB",
        "location": "United Arab Emirates, Dubai",
        "ip_address": "192.168.1.100",
        "mac_address": "00:1A:2B:3C:4D:5E"
    },
    "pc2": {
        "os": "Windows 7",
        "Processor": "Intel Core i5",
        "ram": "16 Gb",
        "video_card": "AMD Radeon RX 580",
        "hard_disk": "2 TB",
        "location": "USA",
        "ip_address": "192.168.1.101",
        "mac_address": "AA:BB:CC:DD:EE:FF"
    },
    "pc3": {
        "os": "Linux",
        "Processor": "AMD Ryzen 7",
        "ram": "32 Gb",
        "video_card": "NVIDIA GeForce RTX 3080",
        "hard_disk": "4 TB",
        "location": "USSR",
        "ip_address": "192.168.1.102",
        "mac_address": "11:22:33:44:55:66"
    }
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computers[device][parameter])


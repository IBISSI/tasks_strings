model = {"TE100-S5":
             {"product Title": "S-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1Gps",
              "Mac adress entries": "2k",
              "Enclozure Material": "Plactic"},
         "TE100-SB":
             {"product Title": "S-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1Gps",
              "Mac adress entries": "1k",
              "Enclozure Material": "Plactic"},
         "TE100-S50g":
             {"product Title": "S-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "5x",
              "Forearding Capacity": "1Gps",
              "Mac adress entries": "1k",
              "Enclozure Material": "Metal Desktop"},
         "TE100-S8Dg":
             {"product Title": "8-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "8x",
              "Forearding Capacity": "1.6Gps",
              "Mac adress entries": "1k",
              "Enclozure Material": "Metal Desktop"},
         "TE100-S16g":
             {"product Title": "16-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "16x",
              "Forearding Capacity": "3.2Gps",
              "Mac adress entries": "8k",
              "Enclozure Material": "Metal Rackmount"},
         "TE100-S24g":
             {"product Title": "24-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "24x",
              "Forearding Capacity": "4.8Gps",
              "Mac adress entries": "8k",
              "Enclozure Material": "Metal Rackmount"}
         }
for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]['Mac adress entries'] == "1k":
        print(model[switch])

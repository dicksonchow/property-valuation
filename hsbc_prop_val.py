import requests
import pandas


hsbc_prop_val_url = "https://rbwm-api.hsbc.com.hk/digital-pws-tools-mortgages-eapi-prod-proxy/v1/mortgages/property-valuation"
client_id = "5eca677638ab454086052a18da4e2cb0"
client_secret = "d35073Cf96B64b1E9CE25f4E07746300"
headers = {"Content-type": "application/json", "client_id": client_id, "client_secret": client_secret}


def invoke_hsbc_prop_val_api(data):
    return requests.post(hsbc_prop_val_url, data=data, headers=headers).json()


def records_to_csv(records, file_name):
    df = pandas.DataFrame.from_dict(records)
    df.to_csv(file_name, encoding="utf-8", index=False)


if __name__ == "__main__":
    '''
    zoneId: [{"id":"1","name":"香港"},{"id":"2","name":"九龍"},{"id":"3","name":"新界/離島"}]
    districtId: [{"id":"36","name":"粉嶺"},{"id":"41","name":"葵涌"},{"id":"49","name":"荔景"},{"id":"44","name":"大嶼山/離島"},{"id":"33","name":"馬鞍山"},{"id":"32","name":"西貢/清水灣"},{"id":"50","name":"深井/青龍頭"},{"id":"38","name":"沙田"},{"id":"35","name":"上水"},{"id":"37","name":"大埔"},{"id":"34","name":"將軍澳"},{"id":"40","name":"青衣"},{"id":"39","name":"荃灣"},{"id":"43","name":"屯門"},{"id":"42","name":"元朗/天水圍"}]}
    '''
    zone_id = 3
    district_id = 33
    estate_id = 1584
    block_id = "nil,7937,nil"
    flat = "A"
    lowest_floor = 3
    highest_floor = 30
    # start of logic
    prop_valuation_records = []
    for floor in range(lowest_floor, highest_floor + 1):
        data = f'{{"locale":"zh_HK","zoneId":"{zone_id}","districtId":"{district_id}","estateId":"{estate_id}","blockId":"{block_id}","floor":"{floor}","flat":"{flat}"}}'
        prop_valuation_records.append(invoke_hsbc_prop_val_api(data))
        print(f"Finished querying the property valuation of floor: {floor}")
    print(f"Finished querying for {highest_floor} floors, generating the csv file...")
    file_name = f"estateId={estate_id}&blockId={block_id}&flat={flat}.csv"
    records_to_csv(prop_valuation_records, file_name)
    print("Finished generating the csv file, enjoy")

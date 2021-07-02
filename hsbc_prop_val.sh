#!/bin/bash

# curl 'https://rbwm-api.hsbc.com.hk/digital-pws-tools-mortgages-eapi-prod-proxy/v1/mortgages/property-valuation' \
#   -H 'Connection: keep-alive' \
#   -H 'Pragma: no-cache' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Content-Type: application/json' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36' \
#   -H 'client_secret: d35073Cf96B64b1E9CE25f4E07746300' \
#   -H 'client_id: 5eca677638ab454086052a18da4e2cb0' \
#   -H 'Accept: */*' \
#   -H 'Sec-GPC: 1' \
#   -H 'Origin: https://www.hsbc.com.hk' \
#   -H 'Sec-Fetch-Site: same-site' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Referer: https://www.hsbc.com.hk/' \
#   -H 'Accept-Language: en-US,en;q=0.9' \
#   --data-raw '{"locale":"zh_HK","zoneId":"3","districtId":"33","estateId":"2372","blockId":"nil,9495,nil","floor":"5","flat":"B"}' \
#   --compressed

curl 'https://rbwm-api.hsbc.com.hk/digital-pws-tools-mortgages-eapi-prod-proxy/v1/mortgages/property-valuation' \
  -H 'Content-Type: application/json' \
  -H 'client_secret: d35073Cf96B64b1E9CE25f4E07746300' \
  -H 'client_id: 5eca677638ab454086052a18da4e2cb0' \
  --data-raw '{"locale":"zh_HK","zoneId":"3","districtId":"33","estateId":"681","blockId":"nil,5797,nil","floor":"36","flat":"E"}' \
  --compressed
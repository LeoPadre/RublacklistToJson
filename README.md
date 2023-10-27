# RublacklistToJson
 Преобразует список заблокированных доменов с сайта rublacklist.net в Json формат

На входе данные вида:

["domain1", "domain12"]

Преобразование в формат:

    [
      {
          "hostname": "domain1",
          "ip": "111.111.111.1111"
      },
      {
          "hostname": "domain2",
          "ip": "222.222.222.222"
      }
    ]

Данный формат подходит для импорта в AmneziaVPN.

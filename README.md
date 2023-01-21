# Storage-API

Данный сервис отвечает за обработку get и post запросов и предоставляет в ответ необходимую информацию или выполняет назначенное действие.
Запросы и ответы отправляются в JSON-формате.

Пример JSON-запроса и ответа на него:
GET-запрос по адресу localhost:8000/get_sensors_name/:

Часть ответа на него:
```
[
    {
        "name": "temp_1",
        "type": "temperature",
        "machine": "oven_1"
    },
    {
        "name": "temp_2",
        "type": "temperature",
        "machine": "oven_1"
    },
    {
        "name": "temp_3",
        "type": "temperature",
        "machine": "oven_2"
    },
    {
        "name": "temp_4",
        "type": "temperature",
        "machine": "oven_2"
    },
    ...
]
```
POST-запрос по адресу localhost:8000/get_sensors_name/:

body:
```
{
    "data_type": "pressure"
}
```

Ответ на него:

```
[
    {
        "name_sensor": "pressure_1",
        "machine": "oven_1"
    },
    {
        "name_sensor": "pressure_2",
        "machine": "oven_1"
    },
    {
        "name_sensor": "pressure_3",
        "machine": "oven_2"
    },
    {
        "name_sensor": "pressure_4",
        "machine": "cooler_1"
    },
    {
        "name_sensor": "pressure_5",
        "machine": "cooler_1"
    },
    {
        "name_sensor": "pressure_6",
        "machine": "cooler_2"
    },
    {
        "name_sensor": "pressure_7",
        "machine": "cooler_2"
    }
]
```
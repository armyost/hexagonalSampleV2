## Installation

python .\src\app\run.py


### Project Map
```
hexagonalSampleV2
├─ README.md
├─ requirements.txt
├─ src
│  └─ app
│     ├─ application
│     │  ├─ exceptions.py
│     │  ├─ services
│     │  │  ├─ department_service.py
│     │  │  ├─ user_service.py
│     │  │  ├─ __init__.py
│     │  └─ __init__.py
│     ├─ controller
│     │  ├─ exceptions.py
│     │  ├─ hr_management.py
│     │  ├─ utils.py
│     │  └─ __init__.py
│     ├─ domain
│     │  ├─ models
│     │  │  ├─ department.py
│     │  │  ├─ user.py
│     │  │  └─ __init__.py
│     │  ├─ repositories
│     │  │  ├─ repository_interface.py
│     │  │  └─ __init__.py
│     │  └─ __init__.py
│     ├─ infrastructure
│     │  ├─ adapters
│     │  │  ├─ mysql_adapter.py
│     │  │  └─ __init__.py
│     │  └─ __init__.py
│     ├─ app.py
│     ├─ configuration.py
│     └─ run.py
└─ tmp
   └─ appmap

```

## Explanation for project componenets
- Application : About Action(include UseCase)
- Controller : Adapter for Client
- Domain.models : Entity (Core)
- Domain.repositories : Port for Database
- Infrastructure.adapter : Adapter for Database

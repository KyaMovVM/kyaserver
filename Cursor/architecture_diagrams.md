# Архитектурные диаграммы: Strategy + Factory Method

Цель: абстракция для удобного понимания, изменения и наблюдения за кодом.

---

## 1. Диаграмма классов (UML) — Strategy + Factory Method

```mermaid
classDiagram
    %% ═══════════════════════════════════════════════════════════
    %% СТРАТЕГИЯ: Абстракция поведения (меняющееся)
    %% ═══════════════════════════════════════════════════════════ 
    
    class Strategy {
        <<interface>>
        +execute(data)*
        +getInfo()* string
    }
    
    class ConcreteStrategyA {
        +execute(data)
        +getInfo() string
    }
    
    class ConcreteStrategyB {
        +execute(data)
        +getInfo() string
    }
    
    class ConcreteStrategyC {
        +execute(data)
        +getInfo() string
    }
    
    Strategy <|.. ConcreteStrategyA
    Strategy <|.. ConcreteStrategyB
    Strategy <|.. ConcreteStrategyC
    
    %% ═══════════════════════════════════════════════════════════
    %% КОНТЕКСТ: Использует стратегию, делегирует работу
    %% ═══════════════════════════════════════════════════════════
    
    class Context {
        -strategy: Strategy
        +setStrategy(strategy: Strategy)
        +performOperation(data)
    }
    
    Context o-- Strategy : использует
    
    %% ═══════════════════════════════════════════════════════════
    %% ФАБРИЧНЫЙ МЕТОД: Абстракция создания объектов
    %% ═══════════════════════════════════════════════════════════
    
    class Creator {
        <<abstract>>
        +factoryMethod()* Strategy
        +someOperation(data)
    }
    
    class ConcreteCreatorA {
        +factoryMethod() Strategy
    }
    
    class ConcreteCreatorB {
        +factoryMethod() Strategy
    }
    
    Creator <|-- ConcreteCreatorA
    Creator <|-- ConcreteCreatorB
    
    Creator ..> Strategy : создаёт
    
    ConcreteCreatorA ..> ConcreteStrategyA : создаёт
    ConcreteCreatorB ..> ConcreteStrategyB : создаёт
```

---

## 2. Структура проекта (пакеты и модули)

```mermaid
flowchart TB
    subgraph "Пакет: core / domain"
        direction TB
        subgraph abstractions["🔹 Абстракции (интерфейсы)"]
            IStrategy["Strategy"]
            ICreator["Creator"]
        end
    end
    
    subgraph "Пакет: strategies"
        direction TB
        S1["ConcreteStrategyA"]
        S2["ConcreteStrategyB"]
        S3["ConcreteStrategyC"]
    end
    
    subgraph "Пакет: factories"
        direction TB
        F1["ConcreteCreatorA"]
        F2["ConcreteCreatorB"]
    end
    
    subgraph "Пакет: context / application"
        direction TB
        Ctx["Context"]
        App["Client / Application"]
    end
    
    IStrategy --> S1
    IStrategy --> S2
    IStrategy --> S3
    
    ICreator --> F1
    ICreator --> F2
    
    Ctx --> IStrategy
    F1 --> S1
    F2 --> S2
    
    App --> Ctx
    App --> F1
    App --> F2
```

---

## 3. Взаимодействие компонентов (Sequence-подобная схема)

```mermaid
sequenceDiagram
    participant Client as Client
    participant Factory as Creator / Factory
    participant Strategy as Strategy
    participant Context as Context
    
    Client->>Factory: createStrategy(type)
    Factory->>Strategy: new ConcreteStrategy()
    Factory-->>Client: strategy
    
    Client->>Context: setStrategy(strategy)
    Context->>Context: сохраняет strategy
    
    Client->>Context: performOperation(data)
    Context->>Strategy: execute(data)
    Strategy-->>Context: result
    Context-->>Client: result
```

---

## 4. Пример реального сценария: Платёжная система

```mermaid
classDiagram
    %% Стратегия: способ оплаты
    class PaymentStrategy {
        <<interface>>
        +pay(amount: float)* bool
        +get_name()* string
    }
    
    class CreditCardPayment
    class PayPalPayment
    class SBPPayment
    class CryptoPayment
    
    PaymentStrategy <|.. CreditCardPayment
    PaymentStrategy <|.. PayPalPayment
    PaymentStrategy <|.. SBPPayment
    PaymentStrategy <|.. CryptoPayment
    
    %% Фабрика: создание стратегии оплаты
    class PaymentFactory {
        <<interface>>
        +create(type, params)* PaymentStrategy
    }
    
    class SimplePaymentFactory {
        +create(type, params) PaymentStrategy
    }
    
    PaymentFactory <|.. SimplePaymentFactory
    
    %% Контекст: корзина
    class ShoppingCart {
        -items: List
        -payment_strategy: PaymentStrategy
        +set_payment_strategy(strategy)
        +checkout() bool
    }
    
    ShoppingCart o-- PaymentStrategy : делегирует
    SimplePaymentFactory ..> PaymentStrategy : создаёт
    
    note for ShoppingCart "Context: не знает деталей оплаты"
    note for SimplePaymentFactory "Инкапсулирует создание стратегий"
```

---

## 5. Принципы для понимания и изменения

```mermaid
flowchart LR
    subgraph "Абстракции"
        A1["Интерфейс Strategy"]
        A2["Интерфейс Creator"]
    end
    
    subgraph "Принципы"
        P1["Открыто/закрыто"]
        P2["Зависимость от абстракций"]
        P3["Единая ответственность"]
    end
    
    subgraph "Результат"
        R1["Понимать: чёткая структура"]
        R2["Изменять: без правок клиента"]
        R3["Наблюдать: логи в стратегиях"]
    end
    
    A1 --> P1
    A2 --> P1
    A1 --> P2
    A2 --> P2
    P1 --> R1
    P2 --> R2
    P3 --> R3
```

---

## 6. Полная UML-схема (комплексный вид)

```mermaid
classDiagram
    direction TB
    
    %% === ИНТЕРФЕЙСЫ ===
    class "<<interface>>\nIStrategy" as IStrategy {
        +execute(data)*
    }
    
    class "<<interface>>\nIFactory" as IFactory {
        +create(type)* IStrategy
    }
    
    %% === КОНТЕКСТ ===
    class "Context" as Context {
        -strategy: IStrategy
        +setStrategy(s)
        +doWork(data)
    }
    
    %% === РЕАЛИЗАЦИИ СТРАТЕГИЙ ===
    class "StrategyA" as SA
    class "StrategyB" as SB
    class "StrategyC" as SC
    
    %% === РЕАЛИЗАЦИИ ФАБРИК ===
    class "FactoryA" as FA {
        +create() StrategyA
    }
    
    class "FactoryB" as FB {
        +create() StrategyB
    }
    
    %% === СВЯЗИ ===
    IStrategy <|.. SA
    IStrategy <|.. SB
    IStrategy <|.. SC
    
    IFactory <|.. FA
    IFactory <|.. FB
    
    Context o--> IStrategy : 1..1
    
    FA ..> SA : создаёт
    FB ..> SB : создаёт
```

---

## Структура файлов проекта (рекомендуемая)

```
src/
├── abstractions/           # Интерфейсы (контракты)
│   ├── strategy.py         # IStrategy
│   └── factory.py          # ICreator / IFactory
│
├── strategies/             # Конкретные стратегии
│   ├── strategy_a.py
│   ├── strategy_b.py
│   └── strategy_c.py
│
├── factories/              # Фабрики создания
│   ├── factory_a.py
│   └── factory_b.py
│
├── context/                # Контекст (использует стратегию)
│   └── context.py
│
└── main.py                 # Точка входа, связывает всё
```

| Слой | Назначение | Изменять |
|------|------------|----------|
| `abstractions/` | Контракты, редко меняются | Почти никогда |
| `strategies/` | Новые алгоритмы, добавлять классы | Добавлять новые файлы |
| `factories/` | Выбор стратегии по условию | При добавлении стратегий |
| `context/` | Бизнес-логика | По необходимости |
| `main.py` | Композиция, запуск | При изменении сценариев |

---

## 7. Архитектура каталогов kyaserver (полная карта проектов)

Цель: абстракция для понимания, изменения и наблюдения. UML-стиль.

```mermaid
flowchart TB
    subgraph kyaserver["📁 kyaserver (монорепозиторий)"]
        direction TB
        
        subgraph infra["🔧 Инфраструктура"]
            dc[.devcontainer]
            cur[.cursor]
            venv[.venv]
            node[node_modules]
            compose[compose.yaml]
            docker[Dockerfile]
        end
        
        subgraph vr["🎯 VR-проекты (Unreal Engine)"]
            direction TB
            subgraph uvr["uvr2026/"]
                u_cfg[Config]
                u_content[Content]
                u_saved[Saved]
                u_inter[Intermediate]
                u_deriv[DerivedDataCache]
                u_proj[*.uproject]
            end
            subgraph myvr["MyVRProject20262/"]
                m_cfg[Config]
                m_content[Content]
                m_saved[Saved]
                m_inter[Intermediate]
                m_deriv[DerivedDataCache]
                m_proj[*.uproject]
            end
        end
        
        subgraph main["main-project/ (основное приложение)"]
            src[src/]
            docs[docs/]
            tests[tests/]
            templates[templates/]
            html[*.html]
        end
        
        subgraph wiki["wiki/ (документация)"]
            w_over[1-overview.md]
            w_build[2-build.md]
        end
        
        subgraph docker_p["docker-projects/"]
            bind[bindmount-apps]
            get[getting-started-app]
            multi[multi-container-app]
        end
        
        subgraph other["Прочие проекты"]
            kya[KyaMovVM.github.io]
            cursor[Cursor/]
            jp[JP/]
            js[JS/]
            draw[drawio/]
            pico[pico4]
            ksp[KSP]
            math[Math]
            tl[todolist]
            en[EN]
            t3b[3b]
        end
    end
    
    kyaserver --> vr
    kyaserver --> main
    kyaserver --> wiki
    kyaserver --> docker_p
    kyaserver --> other
    kyaserver --> infra
```

---

## 8. VR: Strategy + Factory — упрощение архитектуры (ключевое)

VR-проекты содержат много лишнего. Абстракция через Strategy и Factory Method.

```mermaid
classDiagram
    direction TB
    
    %% === АБСТРАКЦИИ (интерфейсы) ===
    class "<<interface>>\nIVRInteractionStrategy" as IVR {
        +interact(context)*
        +getInteractionType()* string
    }
    
    class "<<interface>>\nIVRProjectFactory" as IFactory {
        +createProject(config)* IVRProject
        +createInteraction(type)* IVRInteractionStrategy
    }
    
    class "<<interface>>\nIVRProject" as IProj {
        +loadContent()*
        +getConfig()* Config
    }
    
    %% === VR-проекты как продукты фабрики ===
    class "UVR2026Project" as UVR {
        +loadContent()
        +getConfig()
    }
    
    class "MyVRProject20262" as MyVR {
        +loadContent()
        +getConfig()
    }
    
    %% === Стратегии взаимодействия (общие для VR) ===
    class "DoorInteractionStrategy" as Door
    class "JumpPadInteractionStrategy" as JumpPad
    class "TargetInteractionStrategy" as Target
    
    IVR <|.. Door
    IVR <|.. JumpPad
    IVR <|.. Target
    
    IProj <|.. UVR
    IProj <|.. MyVR
    
    class "VRProjectFactory" as VRF {
        +createProject(name)* IVRProject
        +createInteraction(type)* IVRInteractionStrategy
    }
    
    IFactory <|.. VRF
    VRF ..> UVR : создаёт
    VRF ..> MyVR : создаёт
    VRF ..> Door : создаёт
    VRF ..> JumpPad : создаёт
    VRF ..> Target : создаёт
    
    note for VRF "Упрощает выбор проекта/стратегии"
    note for IVR "Content/LevelPrototyping/Interactable — общая структура"
```

---

## 9. Структура VR Content — что можно абстрагировать

```mermaid
flowchart TB
    subgraph vr_content["VR Content (общая абстракция)"]
        direction TB
        
        subgraph abstractions_layer["🔹 Абстракции (рекомендуемая структура)"]
            I_Interact["IInteractable"]
            I_Asset["IAssetProvider"]
        end
        
        subgraph shared["Общие компоненты (Strategy)"]
            Door[LevelPrototyping/Interactable/Door]
            JumpPad[LevelPrototyping/Interactable/JumpPad]
            Target[LevelPrototyping/Interactable/Target]
        end
        
        subgraph assets["Assets (Factory создаёт)"]
            Meshes[Meshes/]
            Materials[Materials/]
            Textures[Textures/]
        end
        
        subgraph exclude["⚠️ Исключить из версий (лишнее)"]
            Saved[Saved/webcache, logs]
            Derived[DerivedDataCache]
            Interm[Intermediate]
        end
    end
    
    I_Interact --> Door
    I_Interact --> JumpPad
    I_Interact --> Target
    Door --> assets
    JumpPad --> assets
    Target --> assets
```

---

## 10. Полная UML: проекты kyaserver + паттерны

```mermaid
classDiagram
    direction TB
    
    %% === КОРНЕВЫЕ ТИПЫ ПРОЕКТОВ ===
    class "<<abstract>>\nProjectRoot" as Root {
        +name: string
        +getRootPath()* string
        +listFormats()* string[]
    }
    
    class "UnrealVRProject" as URP {
        Config/
        Content/
        Saved/
        Intermediate/
        DerivedDataCache/
    }
    
    class "WebProject" as WP {
        *.html
        src/
        templates/
    }
    
    class "DockerProject" as DP {
        Dockerfile
        compose
    }
    
    class "DocumentationProject" as DocP {
        *.md
    }
    
    Root <|-- URP
    Root <|-- WP
    Root <|-- DP
    Root <|-- DocP
    
    %% === ФАБРИКА ПРОЕКТОВ ===
    class "ProjectFactory" as PF {
        +create(type: ProjectType)* ProjectRoot
        +detectFormat(path)* ProjectType
    }
    
    PF ..> URP : создаёт
    PF ..> WP : создаёт
    PF ..> DP : создаёт
    PF ..> DocP : создаёт
    
    %% === СТРАТЕГИЯ ЗАГРУЗКИ ===
    class "<<interface>>\nILoadStrategy" as ILS {
        +load(project)*
        +validate()* bool
    }
    
    class "UnrealLoadStrategy"
    class "WebLoadStrategy"
    class "DockerLoadStrategy"
    
    ILS <|.. UnrealLoadStrategy
    ILS <|.. WebLoadStrategy
    ILS <|.. DockerLoadStrategy
    
    URP o-- UnrealLoadStrategy : использует
    WP o-- WebLoadStrategy : использует
    DP o-- DockerLoadStrategy : использует
```

---

## 11. Карта корней проектов (все форматы)

```mermaid
mindmap
    root((kyaserver))
        VR Unreal
            uvr2026
            MyVRProject20262
        Web
            main-project
            KyaMovVM.github.io
        Docker
            docker-projects
            compose.yaml
        Документация
            wiki
            Cursor
        Разработка
            JP
            JS
            drawio
            pico4
            KSP
            Math
            todolist
            EN
            3b
        Инфраструктура
            .devcontainer
            .cursor
            .venv
```

---

## 12. Итоговая рекомендация: .gitignore для VR

| Каталог / Файл | Рекомендация | Причина |
|----------------|--------------|---------|
| `Saved/` | Игнорировать | webcache, логи, EditorPerProjectUserSettings |
| `DerivedDataCache/` | Игнорировать | Кэш сборки |
| `Intermediate/` | Игнорировать | Временные артефакты |
| `Content/` | Версионировать | Blueprints, Meshes, Materials — ключевое |
| `Config/` | Версионировать | DefaultEngine, DefaultGame |
| `*.uproject` | Версионировать | Описание проекта |

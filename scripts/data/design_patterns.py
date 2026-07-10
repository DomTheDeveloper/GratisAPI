"""The 23 classic Gang of Four (GoF) software design patterns."""

META = {
    "name": "design_patterns",
    "title": "Design Patterns",
    "description": "The 23 classic Gang of Four object-oriented software design patterns.",
    "emoji": "\U0001F9E9",
}

ITEMS = [
    # --- Creational ---
    {
        "id": "abstract-factory",
        "name": "Abstract Factory",
        "category": "Creational",
        "description": "Provides an interface for creating families of related objects without specifying their concrete classes.",
    },
    {
        "id": "builder",
        "name": "Builder",
        "category": "Creational",
        "description": "Separates the construction of a complex object from its representation so the same process can create different representations.",
    },
    {
        "id": "factory-method",
        "name": "Factory Method",
        "category": "Creational",
        "description": "Defines an interface for creating an object but lets subclasses decide which class to instantiate.",
    },
    {
        "id": "prototype",
        "name": "Prototype",
        "category": "Creational",
        "description": "Creates new objects by copying an existing prototypical instance rather than instantiating from scratch.",
    },
    {
        "id": "singleton",
        "name": "Singleton",
        "category": "Creational",
        "description": "Ensures a class has only one instance and provides a global point of access to it.",
    },
    # --- Structural ---
    {
        "id": "adapter",
        "name": "Adapter",
        "category": "Structural",
        "description": "Converts the interface of a class into another interface clients expect, letting incompatible classes work together.",
    },
    {
        "id": "bridge",
        "name": "Bridge",
        "category": "Structural",
        "description": "Decouples an abstraction from its implementation so the two can vary independently.",
    },
    {
        "id": "composite",
        "name": "Composite",
        "category": "Structural",
        "description": "Composes objects into tree structures to represent part-whole hierarchies, treating individual and composite objects uniformly.",
    },
    {
        "id": "decorator",
        "name": "Decorator",
        "category": "Structural",
        "description": "Attaches additional responsibilities to an object dynamically, providing a flexible alternative to subclassing.",
    },
    {
        "id": "facade",
        "name": "Facade",
        "category": "Structural",
        "description": "Provides a unified, simplified interface to a set of interfaces in a subsystem.",
    },
    {
        "id": "flyweight",
        "name": "Flyweight",
        "category": "Structural",
        "description": "Uses sharing to support large numbers of fine-grained objects efficiently by keeping common state extrinsic.",
    },
    {
        "id": "proxy",
        "name": "Proxy",
        "category": "Structural",
        "description": "Provides a surrogate or placeholder for another object to control access to it.",
    },
    # --- Behavioral ---
    {
        "id": "chain-of-responsibility",
        "name": "Chain of Responsibility",
        "category": "Behavioral",
        "description": "Passes a request along a chain of handlers until one of them handles it, decoupling sender from receiver.",
    },
    {
        "id": "command",
        "name": "Command",
        "category": "Behavioral",
        "description": "Encapsulates a request as an object, allowing parameterization, queuing, logging, and undoable operations.",
    },
    {
        "id": "interpreter",
        "name": "Interpreter",
        "category": "Behavioral",
        "description": "Defines a grammar for a language and an interpreter that uses the representation to interpret sentences in it.",
    },
    {
        "id": "iterator",
        "name": "Iterator",
        "category": "Behavioral",
        "description": "Provides a way to access elements of a collection sequentially without exposing its underlying representation.",
    },
    {
        "id": "mediator",
        "name": "Mediator",
        "category": "Behavioral",
        "description": "Defines an object that encapsulates how a set of objects interact, promoting loose coupling.",
    },
    {
        "id": "memento",
        "name": "Memento",
        "category": "Behavioral",
        "description": "Captures and externalizes an object's internal state so it can be restored later without violating encapsulation.",
    },
    {
        "id": "observer",
        "name": "Observer",
        "category": "Behavioral",
        "description": "Defines a one-to-many dependency so that when one object changes state, all its dependents are notified automatically.",
    },
    {
        "id": "state",
        "name": "State",
        "category": "Behavioral",
        "description": "Allows an object to alter its behavior when its internal state changes, appearing to change its class.",
    },
    {
        "id": "strategy",
        "name": "Strategy",
        "category": "Behavioral",
        "description": "Defines a family of interchangeable algorithms and encapsulates each so they can vary independently of clients.",
    },
    {
        "id": "template-method",
        "name": "Template Method",
        "category": "Behavioral",
        "description": "Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.",
    },
    {
        "id": "visitor",
        "name": "Visitor",
        "category": "Behavioral",
        "description": "Represents an operation to be performed on the elements of an object structure without changing their classes.",
    },
]

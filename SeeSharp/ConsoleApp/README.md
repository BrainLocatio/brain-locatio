# Sentence Storage Console App

## 📌 Project Overview

The application stores sentences and allows the user to add new ones, view existing entries, or delete them.

Project includes the following technical aspects:
- layered architecture
- custom data class
- asynchronous HttpClient
- lazy initialization of HttpClient
- sentence service implements CRUD: save, get, delete
- GUID for unique sentence identification

## Code-level Architecture

The application follows a layered architecture.

### App controller
- **Program.cs** — Serves as the entry point of the application. It handles application startup and coordinates 
interactions between the user interface and the underlying services.

### Presentation Layer 

Responsible for handling user interaction.
- **UI/ConsoleUI.cs** — Contains the console-based user interface logic for displaying data and receiving user input.

### Business Logic Layer

Encapsulates the core functionality of the application.
- **Services/SentenceService.cs** — Handles business operations such as fetching and parsing raw data.

### Data Access Layer

Handles interaction with data storage.

- **Repositories/SentenceRepository.cs** — Manages storage and retrieval of Sentence entries.

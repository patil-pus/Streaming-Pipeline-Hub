  # Integrated Data Pipeline

## Description
This repository contains the implementation of a robust data processing pipeline that integrates several key technologies to manage and analyze real-time data streams efficiently. The system is designed to handle high-throughput data ingestion, processing, and analysis tasks, providing a comprehensive solution for real-time analytics.

## System Architecture
The pipeline architecture is designed to capture data from various APIs, process it through Apache Airflow, and stream it using Apache Kafka with ZooKeeper coordination. Processed data is further analyzed and manipulated using Apache Spark and ultimately stored in Cassandra for persistence. The system also includes a Control Center for monitoring and managing the streaming data flow.

### Components
- **APIs**: Serve as the data sources.
- **Apache Airflow**: Orchestrates and schedules the workflow.
- **Apache Kafka**: Handles the data streaming.
- **ZooKeeper**: Manages and coordinates Kafka.
- **Apache Spark**: Processes the data in real-time.
- **Cassandra**: Stores the processed data.
- **Control Center**: Monitors the health and performance of Kafka clusters.

![image](https://github.com/user-attachments/assets/a752b3db-8173-4e11-b858-d3076aba4547)


## Technologies Used
- Apache Airflow
- Apache Kafka
- ZooKeeper
- Apache Spark
- Cassandra
- PostgreSQL (Assumed for backend storage if APIs interact with databases)

## Setup and Installation
Follow these steps to set up the data processing pipeline in your local environment or production system.

### Prerequisites
- Docker and Docker Compose (for container management)
- Java 11 (required for Kafka and ZooKeeper)
- Python 3.8+ (required for Apache Airflow)
- Node.js (if APIs are JavaScript-based)

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Integrated-Data-Pipeline.git
   cd Integrated-Data-Pipeline

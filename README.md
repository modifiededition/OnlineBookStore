# Online Book Store Microservices

This repository contains an implementation of an online bookstore using two microservices: **Marketplace** and **Recommendations**. The services are designed to work together to provide book recommendations based on user preferences.

## Overview

- **Marketplace**: A Flask web server that communicates with the Recommendations microservice to fetch book recommendations.
- **Recommendations**: A gRPC service that processes requests from the Marketplace and returns a list of book titles based on the specified category and maximum results.

## Directory Structure

The repository contains three main directories:

- **marketplace/**: Contains the code for the Marketplace service.
- **recommendations/**: Contains the code for the Recommendations service.
- **protobufs/**: Contains the Protocol Buffers (proto) file defining the service methods and data types.

### Protocol Buffers Definition

The `protobufs` directory includes a proto file that defines the structure of the service:

```proto
syntax = "proto3";

enum BookCategory {
    MYSTERY = 0;
    SCIENCE_FICTION = 1;
    SELF_HELP = 2;
}

message RecommendationRequest {
    int32 user_id = 1;
    int32 max_results = 2;
    BookCategory category = 3;
}

message BookRecommendation {
    int32 id = 1;
    string title = 2;
}

message RecommendationResponse {
    repeated BookRecommendation recommendation = 1;
}

service Recommendations {
    rpc Recommend (RecommendationRequest) returns (RecommendationResponse);
}
```
## Microservices Implementation

### Marketplace Service

- **Functionality**: When the Marketplace server is accessed at `localhost:5000`, it sends a hardcoded request to the Recommendations microservice with the parameters:
  - `user_id = 1`
  - `max_results = 3`
  - `category = MYSTERY`

- **Response**: The server receives and displays the recommended book titles in the browser.

### Recommendations Service

- **Functionality**: The Recommendations service is implemented using gRPC. It takes a request from the Marketplace and returns a list of book titles based on the given category and the number of titles requested.

## Docker Images

Docker images for both services have been created and hosted on my Docker Hub.

- **Marketplace Image**: `ashishbox/marketplace`
- **Recommendations Image**: `ashishbox/recommendations`

## Kubernetes Configuration

The repository includes Kubernetes YAML files for deploying the services:

- **Pods**: Each service runs in its own pod.
- **Services**: Defines how users can communicate with the Marketplace service and how it interacts with the Recommendations service.

To deploy the services, run:

```bash
kubectl apply -f kubernetes/
```

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/online-book-store.git](https://github.com/modifiededition/OnlineBookStore.git
    ```

2. **Deploy the Services to Your Kubernetes Cluster**:

    ```bash
    kubectl apply -f kubernetes.yml
    ```

5. **Access the Marketplace Service**:

   Open your web browser and navigate to `http://localhost:5000` to view the book recommendations.



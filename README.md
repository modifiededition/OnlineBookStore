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

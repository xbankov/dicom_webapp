# Medical Imaging Coding Assessment

## Overview

This repository contains a web-based platform for processing DICOM (Digital Imaging and Communications in Medicine) images. Users can upload DICOM images, and the system extracts, normalizes, and thresholds the pixel data. After processing, the system displays the volume (in mm³) of the thresholded pixels.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

### Web Interface

- The web interface is implemented using Vue.js and provides a simple page with a drop zone for uploading DICOM images.
- Upon the click on the dropzone it also provides uploadfile menu.
- After processing, the number of pixels above the threshold is displayed.

### Backend

- The backend is built with FastAPI, providing REST endpoints for communication with the web interface.
- The backend uses the Python package pydicom to extract pixel data from DICOM files.
- The pixel data is normalized to a range of [0, 1].
- Thresholding is applied to the pixel data using a threshold value (defaulting to 0.5 if not provided).
- The volume of thresholded pixels in mm³ is returned.

### Docker

- Docker images are provided for both the backend and frontend.
- A docker-compose.yml file is included for running the solution in a Docker environment.

### Code Quality and Testing

- The code is well-documented (by choosing variables names carefully) and partially tested.
- Consideration has been given to various edge cases that might occur when processing DICOM files.

## Setup

### Prerequisites

- Docker and Docker Compose must be installed on your system.

### Instructions

1. Clone this repository to your local machine.

   ```bash
   git clone .git
   ```

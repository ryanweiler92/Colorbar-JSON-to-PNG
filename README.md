# Colorbar JSON File to PNG Sizer

This repository contains a Python script that can convert json files containing colorbar configurations for maps to custom sized PNG files. 

## Prerequisites

To run this script, you need to have the following installed on your system:

- Python 3 (preferably the latest version)

## Setup

1. Clone this repository to your local machine.
2. CD into the repository folder.
3. Create the virtual environment with the command: `python3 -m venv venv`.
4. Activate the virtual environment with the command `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows).
5. Install the required Python packages using the following command in your terminal: `pip install -r requirements.txt`.

## Usage

1. Place any JSON files containing colorbar configurations that you want to convert in the `palettes-custom` directory. This directory currently has 27 color palette configurations from NASA Worldview. These can be removed. 
2. Run the script using the following command in your terminal: `python colorbar-script.py`.
3. The PNG images will generate inside of the `palettes-custom` directory. 
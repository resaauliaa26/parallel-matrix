# Parallel Matrix Multiplication

## Description

This project demonstrates parallel computing using matrix multiplication in Python.

The program divides the matrix computation into multiple processes so each process computes one row of the result matrix.

---

## Flynn's Taxonomy Architecture

### 1. SISD (Single Instruction Single Data)

One processor executes one instruction on one data at a time.
Example: Normal sequential program without parallelism.

### 2. SIMD (Single Instruction Multiple Data)

One instruction operates on multiple data simultaneously.
Example: GPU processing images or performing matrix operations.

### 3. MISD (Multiple Instruction Single Data)

Multiple instructions operate on the same data.
This architecture is rarely used and mostly applied in fault-tolerant systems.

### 4. MIMD (Multiple Instruction Multiple Data)

Multiple processors execute different instructions on different data simultaneously.
Example: Multicore processors and multiprocessing.

---

## Architecture Used in This Project

This program uses **MIMD architecture** because:

- It uses multiple processes (multiprocessing)
- Each process computes a different row of the matrix
- Data is divided among processes
- Computation runs in parallel

---

## How to Run

Run the program using:

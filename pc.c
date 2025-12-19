#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 5

// --- Shared Resources ---
int buffer[BUFFER_SIZE];
int count = 0; // Easier to track count for the API
int in = 0;
int out = 0;

// We remove semaphores here because the API (Python) will handle 
// the "when to call" logic, or we return status codes.

// Initialize the buffer
void init_buffer() {
    for(int i=0; i<BUFFER_SIZE; i++) buffer[i] = -1;
}

// Returns 1 if successful, 0 if full
int produce_item(int item) {
    if (count == BUFFER_SIZE) {
        return 0; // Full
    }
    
    buffer[in] = item;
    in = (in + 1) % BUFFER_SIZE;
    count++;
    return 1; // Success
}

// Returns the item value, or -1 if empty
int consume_item() {
    if (count == 0) {
        return -1; // Empty
    }

    int item = buffer[out];
    buffer[out] = -1; // Visual clear
    out = (out + 1) % BUFFER_SIZE;
    count--;
    return item;
}

// Helper to let Python see the buffer
void get_buffer_state(int *target_array) {
    for(int i=0; i<BUFFER_SIZE; i++) {
        target_array[i] = buffer[i];
    }
}

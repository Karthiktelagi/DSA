# Notes

- `(n & 1)` extracts the last bit.
- `result << 1` makes space for the next bit.
- `|` inserts the extracted bit.
- `n >>= 1` removes the processed bit.
- Loop runs exactly 32 times for a 32-bit integer.
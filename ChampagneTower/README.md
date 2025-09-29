# Champagne Tower Simulator

This is a simple student project that simulates pouring champagne into a tower of glasses. Each glass can hold 1 unit of champagne. If a glass overflows, the excess is split equally to the two glasses immediately below it.

---

## How it works

1. You pour a certain amount of champagne into the top glass.
2. Champagne flows down the tower according to the rules:
   - Each glass can hold a maximum of 1 unit.
   - Any extra amount is equally split to the left and right glass below.
3. The program calculates how much champagne is in a specific glass that you choose.

---

## Inputs

The program will ask for **three inputs**:

1. **Total poured amount (`float`)**

   - This is the total champagne poured into the top glass.
   - Example: `10` (10 units of champagne poured).

2. **Row number (`int`)**

   - The row of the glass you want to check.
   - Row numbering starts at `1` (the top glass is row 1).
   - Example: `5` (check a glass in the third row).

3. **Glass number (`int`)**
   - The position of the glass in that row.
   - Glass numbering starts at `1` from the left.
   - Example: `3` (the second glass in the row).

---

## Output

- The program prints the **amount of champagne in the chosen glass**.
- The amount is capped at 1 unit (the glass cannot hold more than 1).
- Example output:
  ```
  Amount in the glass: 0.625
  ```

---

## Notes

- The program uses a simple **2D array** to simulate the tower.
- Only works for reasonable tower sizes (up to row 100).
- Extra messages are printed to make it clear which glass and row are being calculated.
- Press **Enter** at the end to close the program so the `.exe` doesn’t close immediately.

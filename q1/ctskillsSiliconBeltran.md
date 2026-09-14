# Computational Thinking Exercise

## Smart School Canteen Queue

**Name:** Kassandra A. Beltran

**Section:** Silicon

**Last Name:** Beltran

**Date:** August 20, 2026
---

## Step 1: Identify the Big Problem

### Main Problem

The PSHS school canteen is small, overcrowded, and operates on a slow and inefficient payment and ordering process during lunch breaks.

---

## Step 2: Identify the Sub-Problems

1. Slow Decision-Making: Students take too long to view the menu and decide what to order while standing at the counter.

2. Manual Transaction and Calculation: Cashiers manually compute the total bill amounts and count change by hand, slowing down checkout time.

3. Lack of Inventory Tracking: There is no automated system to monitor available food inventory in real time, causing stock to run out unexpectedly.

4. Physical Congestion: A small physical layout paired with long queus leads tosevere crowding during peak lunch hours.

---

## Step 3: Apply Computational Thinking Skills

| Slow Decision-Making | Pattern Recognition | Display a digital menu board outside the queue and allow pre-ordering based on peak ordering trends. |

| Manual Transaction and Calculation | Algorithm Design | Implement an automated system that instantly totals prices and calculates exact change. |

| Lack of Inventory Tracking | Abstraction | Build a digital inventory tracking system that automatically updates stock counts with each sale and hides out-of-stock items. |

| Physical Congestion | Decomposition | Break down the service line into separate designated counters for ordering, payment, and meal pick-up. |

---
## Step 4: Algorithmic Solution

### Selected Sub-Problem

Manual Transaction and Calculation

### Pseudocode

START
  SET totalBill = 0
  SET itemPrice = 0
  SET paymentAmount = 0
  SET change = 0

  WHILE more items to scan
    INPUT itemPrice
    totalBill += itemPrice
  END WHILE

  DISPLAY totalBill

  REPEAT
    INPUT paymentAmount
    IF paymentAmount < totalBill THEN
      DISPLAY "Insufficient payment. Enter a higher amount."
    END IF
  UNTIL paymentAmount >= totalBill

  change = paymentAmount - totalBill
  DISPLAY "Change due: ", change
  DISPLAY "Transaction Complete"
END

---

43. No forward sales without ownership (bai’ al-salam):
    - Forward sales are allowed only if the seller actually owns the goods being sold and can deliver them at the specified time.
    - Example: Selling crops that have not yet been planted without proper conditions.
    - Solidity Example:
      ```solidity
      // Compliant: Forward sales with ownership
      contract ForwardSale {
          address public seller;
          address public buyer;
          string public goods;
          uint256 public deliveryDate;
```solidity// Compliant: Forward sales with ownership
      contract ForwardSale {
          address public seller;
          address public buyer;
          string public goods;
          uint256 public deliveryDate;
```
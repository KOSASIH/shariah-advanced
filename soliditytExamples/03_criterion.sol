3. No involvement in gharar (excessive uncertainty): 
    - The contract must avoid excessive uncertainty and ambiguity in its terms and conditions.
    - Example: A contract for the sale of goods where the quantity or quality of goods is not clearly defined.
    - Solidity Example:
      ```solidity
      // Not compliant: Sale of undefined goods
      contract Sale {
          uint256 public price;
          address public seller;
          address public buyer;
          string public goods;
```solidity// Not compliant: Sale of undefined goods
      contract Sale {
          uint256 public price;
          address public seller;
          address public buyer;
          string public goods;
```
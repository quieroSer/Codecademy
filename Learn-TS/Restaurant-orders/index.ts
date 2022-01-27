import { restaurants, Restaurant } from "./restaurants";
import { orders, Order, PriceBracket } from "./orders";

/// Add your getMaxPrice() function below:
function getMaxPrice(priceBracket: PriceBracket): number {
  if(priceBracket === PriceBracket.Low) {
    return 10
  } else if (priceBracket === PriceBracket.Medium) {
    return 20
  } else if (priceBracket === PriceBracket.High) {
    return 30
  } else {
    return NaN
  }
}
/// Add your getOrders() function below:
function getOrders(price: PriceBracket, orders: Order[][]): Order[][] {
  let filteredOrders: Order[][] = [];
  const limit: number = getMaxPrice(price) 
  orders.forEach(rest => {
    let result = rest.filter( o => o.price <= limit)
    filteredOrders.push(result)
  })
  return filteredOrders
}
/// Add your printOrders() function below:
function printOrders(rest: Restaurant[], orders: Order[][]): void {
  rest.forEach( (r: Restaurant, index: number) => {
    if(orders[index].length > 0) {
      console.log(r.name)
      let total: number = 0
      orders[index].forEach( (o: Order, index: number) => {
        console.log(`Order ${index+1}: ${o.name} is $${o.price}`)
        total += o.price
      })
      console.log(`Total: $${total}`)
    }
  
  })
}


/// Main
const elligibleOrders = getOrders(PriceBracket.Low, orders);
printOrders(restaurants, elligibleOrders);

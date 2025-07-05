import dagster as dg 
import time 

@dg.asset(kinds=["facebook"])
def Hello(context: dg.AssetExecutionContext):
    context.log.info("Hello!")


@dg.asset(kinds=["instagram"],deps=[Hello])
def World(context: dg.AssetExecutionContext):
    context.log.info("World!")

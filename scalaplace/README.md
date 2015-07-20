This is a simple Scala version of the Laplace demo.

Run this by installing the Typesafe Activator at: https://www.typesafe.com/get-started - you can install a recent Java
and get the no-bundled-dependencies version.
 
 
Then run:

> SBT_OPTS="-Xmx4G" $path_to_activator/activator test  

It should print out the average time per-iteration for the 15k Laplace case.
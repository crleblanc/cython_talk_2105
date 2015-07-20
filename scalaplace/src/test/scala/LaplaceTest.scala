import org.scalatest._
import org.scalatest.matchers.ShouldMatchers

class LaplaceTest extends FunSuite with Matchers {

  test("simple laplace performance test") {

    val (dx, dy) = (0.1, 0.1)

    val (dx2, dy2) = (dx*dx, dy*dy)

    val size = 15000
    val arr = Array.fill(size)(
      Array.fill(size)(0.0)
    )

    (1 to 10).foreach { _ =>
      resetArr(arr)
      Laplace.laplace(arr, dx2, dy2)
    }

    var totalDuration = 0l
    val iterations = 10
    (1 to iterations).foreach { _ =>

      resetArr(arr)
      val start = System.currentTimeMillis()
      Laplace.laplace(arr, dx2, dy2)

      totalDuration += System.currentTimeMillis() - start
    }

    print("Avg time per iteration: %2.2f".format(totalDuration / iterations.toDouble))

  }

  def resetArr(arr: Array[Array[Double]]): Unit = {

    for (i <- arr.indices;
         j <- arr(i).indices) {

      arr(i)(j) = 0
    }

    arr(0)(0) = 1.0
  }
}

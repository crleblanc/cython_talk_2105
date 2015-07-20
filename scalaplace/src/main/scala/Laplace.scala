object Laplace {

  // NOTE: this mutates the array
  def laplace(arr: Array[Array[Double]], dx2: Double, dy2: Double): Unit = {

    1 until (arr.length - 1) foreach { i =>

      // NOTE: could grab this from the 0th array and cache it
      1 until (arr(i).length - 1) foreach { j =>

        arr(i)(j) =
          ((arr(i + 1)(j) + arr(i - 1)(j)) * dx2 +
            (arr(i)(j + 1) + arr(i)(j - 1) * dx2)) /
            (2 * (dx2 + dy2))

      }
    }
  }

}

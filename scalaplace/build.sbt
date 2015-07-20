name := """scalaplace"""

version := "1.0"

scalaVersion := "2.11.0"

resolvers += "Sonatype OSS Snapshots" at
  "https://oss.sonatype.org/content/repositories/releases"

libraryDependencies += "org.scalatest" % "scalatest_2.11" % "2.1.3" % "test"

libraryDependencies += "org.scala-lang.modules" % "scala-xml_2.11" % "1.0.1"

libraryDependencies += "com.storm-enroute" %% "scalameter" % "0.6"

testFrameworks += new TestFramework("org.scalameter.ScalaMeterFramework")

parallelExecution in Test := false



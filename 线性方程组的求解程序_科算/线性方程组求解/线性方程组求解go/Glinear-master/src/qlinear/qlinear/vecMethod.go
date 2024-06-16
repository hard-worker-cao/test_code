package qlinear

import "math"



func (x Vec3f) norm() float32 {
	return sqrt(x.F1*x.F1 + x.F2*x.F2 + x.F3*x.F3)
}

//float32的开方
func sqrt(x float32) float32 {
	var xhalf float32 = 0.5 * x // get bits for floating VALUE
	i := math.Float32bits(x)    // gives initial guess y0
	i = 0x5f375a86 - (i >> 1)   // convert bits BACK to float
	x = math.Float32frombits(i) // Newton step, repeating increases accuracy
	x = x * (1.5 - xhalf*x*x)
	x = x * (1.5 - xhalf*x*x)
	x = x * (1.5 - xhalf*x*x)
	return x
}

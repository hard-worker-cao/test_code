package qlinear

//Vec3f3维float Vec
type Vec3f struct {
	F1 float32
	F2 float32
	F3 float32
}

type Vec3i struct {
	I1 int8
	I2 int8
	I3 int8
}

/*二维Vec*/

type Vec2f struct {
	F1 float32
	F2 float32
}

type Vec2i struct {
	I1 int8
	I2 int8
}

/*多维Vec*/

type Veci struct {
	I []int8
}

type Vecf struct {
	F []float32
}

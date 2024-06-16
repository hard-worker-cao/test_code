package qlinear

//Vec3f的二元运算

func Vec3fAdd(v1, v2, res *Vec3f) {
	res.F1 = v1.F1 + v2.F1
	res.F2 = v1.F2 + v2.F2
	res.F3 = v1.F3 + v2.F3
}

func CrossProduct(u, v, res *Vec3f) {
	res.F1 = u.F2*v.F3 - u.F3*v.F2
	res.F2 = u.F3*v.F1 - u.F1*v.F3
	res.F3 = u.F1*v.F2 - u.F2*v.F1

}

func InnerProduct(u *Vec3f, v *Vec3f, res *float32) {
	*res = u.F1*v.F1 + u.F2*v.F2 + u.F3*v.F3
}

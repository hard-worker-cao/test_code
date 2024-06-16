package qlinear

import "testing"

func TestVec3fAdd(t *testing.T) {
	v1 := Vec3f{1.0, 0.2, 0.3}
	v2 := Vec3f{2.0, 0.5, -0.8}
	var v3 Vec3f
	Vec3fAdd(&v1, &v2, &v3)
	flag1 := (v3.F1 == 3.0)
	flag2 := (v3.F2 == 0.7)
	flag3 := (v3.F3 == -0.5)
	if !(flag1 && flag2 && flag3) {
		t.Error("Vec3fAdd() error!\n")
	}
}

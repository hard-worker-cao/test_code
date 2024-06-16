package qlinear

type Quad struct {
	q0 float32
	q1 float32
	q2 float32
	q3 float32
}

func (quad *Quad) S() float32 {
	return quad.q0
}

func (quad *Quad) V() Vec3f {
	return Vec3f{quad.q1, quad.q2, quad.q3}
}

func (quad Quad) Conj() Quad {
	return Quad{q0: quad.q0, q1: -quad.q1, q2: -quad.q2, q3: -quad.q3}
}

func (q_a Quad) Add(q_b Quad) Quad {
	return Quad{q0: q_a.q0 + q_b.q0,
		q1: q_a.q1 + q_b.q1,
		q2: q_a.q2 + q_b.q2,
		q3: q_a.q3 + q_b.q3}
}

func (q_a Quad) MultQuad(q_b Quad) Quad {
	return Quad{
		q0: q_a.q0 * q_b.q0,
	}
}

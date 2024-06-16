package qlinear

type MatInvariant interface {
	Deter() int
	Tracer() int
}

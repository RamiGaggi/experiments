package ch1

import "testing"

func BenchmarkEchoArgsEffective(b *testing.B) {
	for i:= 0; i < b.N; i++ {
		EchoArgs1()
	}
}

func BenchmarkEchoArgsUnEffective(b *testing.B) {
	for i:= 0; i < b.N; i++ {
		EchoArgs4()
	}
}

package main

import (
    "golang.org/x/mobile/app"
    "golang.org/x/mobile/event/lifecycle"
    "golang.org/x/mobile/event/paint"
    "golang.org/x/mobile/gl"
)

func main() {
    app.Main(func(a app.App) {
        var glCtx *gl.Context
        for ev := range a.Events() {
            switch ev := a.FilterEvent(ev).(type) {
            case lifecycle.Event:
                if ev.Crosses(lifecycle.StageVisible) {
                    glCtx, _ = gl.NewContext()
                }
            case paint.Event:
                if glCtx == nil {
                    continue
                }
                defer ev.Done()
                glCtx.ClearColor(1, 1, 1, 1)
                glCtx.Clear(gl.COLOR_BUFFER_BIT)
            }
        }
    })
}

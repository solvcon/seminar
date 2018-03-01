# SOLVCON Development Planning 2018Q1

[Markdown version](https://github.com/solvcon/seminar/blob/gh-pages/2018/plan18q1/index.md) of this page.

* Where: 工學院綜合大樓 727 室 (Engineering Building Rm 727)
* When: 2018/3/2 15:00-17:00
* [Sign-up sheet](https://github.com/solvcon/seminar/issues/8)
* [Agenda](#agenda)

Last updated: 2018/2/22

## <a name="agenda"></a>Agenda

| Time          | Topic                                    | Presenter |
| :------------ | :--------------------------------------- | --------- |
| 15:00 - 15:25 | Dev Plan 18Q1                            | Yung-Yu   |
| 15:25 - 15:40 | [Research Group Status Quo](#statusquo)  | Yung-Yu   |
| 15:40 - 16:05 | Modern Virtualization Technologies       | Taihsiang |
| 16:05 - 16:20 | Career Opportunities with Virtualization | Taihsiang |
| 16:20 - 16:30 | [Immediate Deliverables](#deliverables)  | Yung-Yu   |

## <a name="statusquo"></a>Research Group Status Quo

* Computer / server farm (facility)?
* Version control?
* Testing strategy / coverage?
* Code review?
* Continuous integration?

## <a name="deliverables"></a>Immediate Deliverables

Maybe we can make the plan clearer, or maybe not.  It’s highly unlikely to come up with a schedule, though.

* Test 3D Euler solver (`march::gas`)
* Distill the CESE solver (`march::cese`)
* (Re-)enable message-passing parallelism (`march::mp`)
* Develop granular flow solver `march::gran`
* Develop Navier-Stokes solver (together in `march::gas`)

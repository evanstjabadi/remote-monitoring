import React from "react";
import { Chart } from "react-charts";

export default function Graphs() {
  const data = [
    {
      label: "label 1",
      data: [
        [new Date("2017-05-04"), 11],
        [new Date("2018-05-04"), 22],
        [new Date("2019-05-04"), 14],
        [new Date("2020-05-04"), 21],
        [new Date("2020-05-04"), 21],
        [new Date("2020-05-04"), 23],
        [new Date("2020-05-04"), 4],
        [new Date("2020-05-04"), 21],
        [new Date("2021-05-04"), 7]
      ]
    }
  ];

  const axes = [
    { primary: true, type: "time", position: "bottom" },
    { type: "linear", position: "left" }
  ];

  return (
    <div
      style={{
        width: "400px",
        height: "300px"
      }}
    >
      <Chart data={data} axes={axes} />
    </div>
  );
}

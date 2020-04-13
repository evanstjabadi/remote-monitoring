import React, { useEffect, useState } from 'react'
import { Chart } from 'react-charts'

export default function Graphs() {
  const [apidata, setAPIData] = useState()
  useEffect(() => {
    fetch('https://remote-monitoring.evanstjabadi.live/backend/randoms/')
      .then((response) => response.json())
      .then((data) => {
        setAPIData(data)
      })
  }, [])

  if (!apidata) return 'Loading...'

  const dataPoints = apidata.map((point) => {
    return [new Date(point.time_stamb), point.value]
  })

  const data = [
    {
      label: 'label 1',
      data: dataPoints,
    },
  ]

  const axes = [
    { primary: true, type: 'time', position: 'bottom' },
    { type: 'linear', position: 'left' },
  ]

  return (
    <div
      style={{
        width: '400px',
        height: '300px',
      }}
    >
      <Chart data={data} axes={axes} />
    </div>
  )
}

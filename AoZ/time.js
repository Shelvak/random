const numberToTime = (number) => {
  d = Number(number);
  var m = Math.floor(d % 3600 / 60).toString();
  var s = Math.floor(d % 3600 % 60).toString();

  return `${m.padStart(1, '0')}:${s.padStart(2, '0')}`
}

const samplingFromNumber = (number, seconds=30) => {
  if (number <= 30) {
    return [number]
  } else {
    return [number].concat(samplingFromNumber(number - seconds, seconds))
  }
}

const for25 = (n) => { return n - parseInt(n * 0.25) }
const for50 = (n) => { return parseInt(n * 0.5) }

const toNumber = (value) => {
  if (/\d+\D\d+/.test(value)) {
    parts = value.split(/\D/).map((n) => Number(n))

    switch (parts.length) {
      case 1:
        number =  Number(parts[0]);
        break
      case 2:
        number =  Number(parts[0] * 60 + parts[1])
        break
      default:
        number =  Number(parts[0] * 3600 + parts[1] * 60 + parts[0])
        break
    }
  } else {
    number = Number(value)
  }

  return number
}

const tableWithDiff = (number, rawDiff) =>  {
  let diff = toNumber(rawDiff)
  let sampling = samplingFromNumber(number, 1);

  console.log(`${"T1".padStart(10)} | ${"25%".padStart(10)} | ${"50%".padStart(10)}`)
  for (let i = 0; i < sampling.length; i++) {
    if (i % 30 == 0) {
      let t = sampling[i]
      console.log(`${`${numberToTime(t)}`.padStart(10)} | ${numberToTime(for25(t)).padStart(10)} | ${numberToTime(for50(t)).padStart(10)}`)
    }
  }

  let w25 = sampling.find((t) => t - diff == for25(t))
  let w50 = sampling.find((t) => t - diff == for50(t))
  console.log(`\nIdeal: 25% => ${numberToTime(w25)}  50% => ${numberToTime(w50)}`)
}

const table = (number) =>  {
  let sampling = samplingFromNumber(number);

  console.log(`${"T1".padStart(10)} | ${"25%".padStart(10)} | ${"50%".padStart(10)}`)
  for (let i = 0; i < sampling.length; i++) {
    let t = sampling[i]
    console.log(`${`${numberToTime(t)}`.padStart(10)} | ${numberToTime(for25(t)).padStart(10)} | ${numberToTime(for50(t)).padStart(10)}`)
  }
}


const _number = toNumber(process.argv[2])

if (process.argv[3]) {
  tableWithDiff(_number, process.argv[3])
} else {
  table(_number)
}

const cel = Number.parseFloat(prompt("Введите температуру в градусах Цельсия"));
const Fahr = (9 / 5) * cel + 32;
alert(`Цельсий: ${cel}, Фаренгейт: ${Fahr.toFixed(1)}`);

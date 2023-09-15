import React from "react";

const CustomButton = ({ functie, classStyle, text, textStyle }) => {
  return (
    <button onClick={functie} className={classStyle}>
      <h1 className={textStyle}>{text}</h1>
    </button>
  );
};

export default CustomButton;

import React from "react";

const CustomButton = ({ functie, classStyle, text }) => {
  return (
    <button onClick={functie} className={classStyle}>
      {text}
    </button>
  );
};

export default CustomButton;

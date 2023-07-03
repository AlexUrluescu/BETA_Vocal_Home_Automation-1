import React from "react";

const InfoMessage = ({ styleHeating, classStyle, textStyle, text }) => {
  return (
    <div className={classStyle}>
      {styleHeating === 1 ? (
        <p className={textStyle}>
          {text}
        </p>
      ) : (
        <p> </p>
      )}
    </div>
  );
};

export default InfoMessage;
